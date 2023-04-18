import adsk.core, adsk.fusion, adsk.cam, traceback

app = adsk.core.Application.get()
ui  = app.userInterface
# ui.messageBox('Hello script')

active_document = app.activeDocument


new_document = app.documents.add(adsk.core.DocumentTypes.FusionDesignDocumentType)

if active_document:
    active_document.close(False)

