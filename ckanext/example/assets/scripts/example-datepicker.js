/**
 * Daterangepicker adapter.
 * https://www.daterangepicker.com/
 */
ckan.module("example-datepicker", function ($) {
  return {
    options: {},

    initialize() {
      // stop execution if dependency is missing.
      if (typeof $.fn.daterangepicker === "undefined") {
        // reporting the source of the problem is always a good idea.
        console.error(
          "[example-datepicker] daterangepicker library is not loaded",
        );
        return;
      }

      const options = this.sandbox["example"].nestedOptions(
        this.options,
      );

      this.el.daterangepicker(options);
    },
  };
});
