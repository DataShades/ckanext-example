/**
 * OverlayScrollbars adapter.
 * https://kingsora.github.io/OverlayScrollbars/
 */
ckan.module("example-scrollbar", function ($) {
  return {
    options: {},

    initialize() {
      // stop execution if dependency is missing.
      if (typeof OverlayScrollbarsGlobal === "undefined") {
        // reporting the source of the problem is always a good idea.
        console.error(
          "[example-scrollbar] OverlayScrollbars library is not loaded",
        );
        return;
      }

      const options = this.sandbox["example"].nestedOptions(
        this.options,
      );

      OverlayScrollbarsGlobal.OverlayScrollbars(this.el[0], options)
    },
  };
});
