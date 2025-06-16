import { useTheme } from "$/utils/react-theme";
import { useColorMode as chakraUseColorMode } from "@chakra-ui/react";
import { createElement, useEffect } from "react";
import { ColorModeContext, defaultColorMode } from "$/utils/context";

export default function ChakraColorModeProvider({ children }) {
  const { theme, resolvedTheme, setTheme } = useTheme();
  const { colorMode: chakraColorMode, toggleColorMode: toggleChakraColorMode } =
    chakraUseColorMode();

  useEffect(() => {
    if (chakraColorMode != resolvedTheme) {
      toggleChakraColorMode();
    }
  }, [theme, resolvedTheme]);

  const toggleColorMode = () => {
    setTheme(resolvedTheme === "light" ? "dark" : "light");
  };

  const setColorMode = (mode) => {
    const allowedModes = ["light", "dark", "system"];
    if (!allowedModes.includes(mode)) {
      console.error(
        `Invalid color mode "${mode}". Defaulting to "${defaultColorMode}".`
      );
      mode = defaultColorMode;
    }
    setTheme(mode);
  };

  return createElement(
    ColorModeContext.Provider,
    {
      value: {
        rawColorMode: theme,
        resolvedColorMode: resolvedTheme,
        toggleColorMode,
        setColorMode,
      },
    },
    children
  );
}
