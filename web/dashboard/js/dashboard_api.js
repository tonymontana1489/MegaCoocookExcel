// Bridge between the web dashboard and the Python API (PyWebView).
window.dashboardApi = window.pywebview?.api ?? {
  async importPdf(pdfPath) {
    return {
      success: false,
      message: "Keine Python-Bridge verfügbar."
    };
  }
};
