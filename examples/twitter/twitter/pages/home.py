"""The home page. This file includes examples abstracting complex UI into smaller components."""
import reflex as rx
import reflex_chakra as rc
from twitter.state.base import State
from twitter.state.home import HomeState

from ..components import container


def tab_button(name, href):
    """A tab switcher button."""
    return rc.link(
        rc.icon(tag="star", mr=2),
        name,
        display="inline-flex",
        align_items="center",
        py=3,
        px=6,
        href=href,
        border="1px solid #eaeaea",
        font_weight="semibold",
        border_radius="full",
    )


def tabs():
    """The tab switcher displayed on the left."""
    return rc.box(
        rc.vstack(
            rc.heading("PySocial", size="md"),
            tab_button("Home", "/"),
            rc.box(
                rc.heading("Followers", size="sm"),
                rx.foreach(
                    HomeState.followers,
                    lambda follow: rc.vstack(
                        rc.hstack(
                            rc.avatar(name=follow.follower_username, size="sm"),
                            rc.text(follow.follower_username),
                        ),
                        padding="1em",
                    ),
                ),
                p=4,
                border_radius="md",
                border="1px solid #eaeaea",
            ),
            rc.button("Sign out", on_click=State.logout),
            align_items="left",
            gap=4,
        ),
        py=4,
    )


def sidebar(HomeState):
    """The sidebar displayed on the right."""
    return rc.vstack(
        rc.input(
            on_change=HomeState.set_friend,
            placeholder="Search users",
            width="100%",
        ),
        rx.foreach(
            HomeState.search_users,
            lambda user: rc.vstack(
                rc.hstack(
                    rc.avatar(name=user.username, size="sm"),
                    rc.text(user.username),
                    rc.spacer(),
                    rc.button(
                        rc.icon(tag="add"),
                        on_click=lambda: HomeState.follow_user(user.username),
                    ),
                    width="100%",
                ),
                py=2,
                width="100%",
            ),
        ),
        rc.box(
            rc.heading("Following", size="sm"),
            rx.foreach(
                HomeState.following,
                lambda follow: rc.vstack(
                    rc.hstack(
                        rc.avatar(name=follow.followed_username, size="sm"),
                        rc.text(follow.followed_username),
                    ),
                    padding="1em",
                ),
            ),
            p=4,
            border_radius="md",
            border="1px solid #eaeaea",
            w="100%",
        ),
        align_items="start",
        gap=4,
        h="100%",
        py=4,
    )


def feed_header(HomeState):
    """The header of the feed."""
    return rc.hstack(
        rc.heading("Home", size="md"),
        rc.input(on_change=HomeState.set_search, placeholder="Search tweets"),
        justify="space-between",
        p=4,
        border_bottom="1px solid #ededed",
    )


def composer(HomeState):
    """The composer for new tweets."""
    return rc.grid(
        rc.vstack(
            rc.avatar(size="md"),
            p=4,
        ),
        rc.box(
            rc.text_area(
                w="100%",
                border=0,
                placeholder="What's happening?",
                resize="none",
                py=4,
                px=0,
                _focus={"border": 0, "outline": 0, "boxShadow": "none"},
                on_blur=HomeState.set_tweet,
            ),
            rc.hstack(
                rc.button(
                    "Tweet",
                    on_click=HomeState.post_tweet,
                    bg="rgb(29 161 242)",
                    color="white",
                    border_radius="full",
                ),
                justify_content="flex-end",
                border_top="1px solid #ededed",
                px=4,
                py=2,
            ),
        ),
        grid_template_columns="1fr 5fr",
        border_bottom="1px solid #ededed",
    )


def tweet(tweet):
    """Display for an individual tweet in the feed."""
    return rc.grid(
        rc.vstack(
            rc.avatar(name=tweet.author, size="sm"),
        ),
        rc.box(
            rc.text("@" + tweet.author, font_weight="bold"),
            rc.text(tweet.content, width="100%"),
        ),
        grid_template_columns="1fr 5fr",
        py=4,
        gap=1,
        border_bottom="1px solid #ededed",
    )


def feed(HomeState):
    """The feed."""
    return rc.box(
        feed_header(HomeState),
        composer(HomeState),
        rx.cond(
            HomeState.tweets,
            rx.foreach(
                HomeState.tweets,
                tweet,
            ),
            rc.vstack(
                rc.button(
                    rc.icon(
                        tag="repeat",
                        mr=1,
                    ),
                    rc.text("Click to load tweets"),
                    on_click=HomeState.get_tweets,
                ),
                p=4,
            ),
        ),
        border_x="1px solid #ededed",
        h="100%",
    )


def home():
    """The home page."""
    return container(
        rc.grid(
            tabs(),
            feed(HomeState),
            sidebar(HomeState),
            grid_template_columns="1fr 2fr 1fr",
            h="100vh",
            gap=4,
        ),
        max_width="1300px",
    )
