import QtQuick 2.12
import QtQuick.Controls 2.12
import QtQuick.Controls.Basic 2.12

ApplicationWindow {
    id: mainWindow
    visible: true
    width: 960
    height: 575
    minimumWidth: 480
    minimumHeight: 270
    title: "CHAD: Chat CAD"

    flags: Qt.Window | Qt.WindowTitleHint | Qt.WindowSystemMenuHint | Qt.WindowCloseButtonHint


    property int text_field_width: 150
    property int text_field_height: 30
    property int top_margin: 30
    property int left_margin: 30
    property int top_margin_sub: 10

    property bool generateButtonEnabled: true


    //buttons
    property int button_width: 150
    property int button_height: 50


    Rectangle {
        anchors.fill: parent
        color: "#190500"

        Text {
            id: text_enter_api_key
            anchors.left: parent.left
            anchors.leftMargin: 30
            anchors.top: parent.top
            anchors.topMargin: 20
            color: "#ffffff"
            text: qsTr("Enter API KEY:")
            font.pixelSize: 16
            //make bold
            font.bold: true
        }
        TextField {
            id: text_field_api_key
            anchors.left: parent.left
            anchors.leftMargin: left_margin
            anchors.top: text_enter_api_key.bottom
            anchors.topMargin: top_margin_sub
            width: text_field_width
            height: text_field_height
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
            font.italic: true
            placeholderText: qsTr("API KEY")
            font.pixelSize: 16
            Component.onCompleted: {
                text = pyInterface.api_key_qml
            }

            background: Rectangle {
                implicitHeight: text_field_width
                implicitWidth: text_field_height
                color: "white"
                radius: 8
            }
        }

        Text {
            id: text_enter_port
            anchors.left: parent.left
            anchors.leftMargin: left_margin
            anchors.top: text_field_api_key.bottom
            anchors.topMargin: top_margin
            color: "#ffffff"
            text: qsTr("Enter Port #:")
            font.pixelSize: 16
            font.bold: true
        }
        TextField {
            id: text_field_port
            anchors.left: parent.left
            anchors.leftMargin: left_margin
            anchors.top: text_enter_port.bottom
            anchors.topMargin: top_margin_sub
            width: text_field_width
            height: text_field_height
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
            font.italic: true
            placeholderText: qsTr("Enter Port")
            font.pixelSize: 16
            
            Component.onCompleted: {
                text = pyInterface.port_qml
            }

            background: Rectangle {
                implicitHeight: text_field_width
                implicitWidth: text_field_height
                color: "white"
                radius: 8
            }
        }

        Text {
            id: text_file_name
            anchors.left: parent.left
            anchors.leftMargin: left_margin
            anchors.top: text_field_port.bottom
            anchors.topMargin: top_margin
            color: "#ffffff"
            text: qsTr("Enter file name:")
            font.pixelSize: 16
            font.bold: true
        }
        TextField {
            id: text_field_filename
            anchors.left: parent.left
            anchors.leftMargin: left_margin
            anchors.top: text_file_name.bottom
            anchors.topMargin: top_margin_sub
            width: text_field_width
            height: text_field_height
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
            font.italic: true
            placeholderText: qsTr("Enter File Name")
            font.pixelSize: 16
            
            Component.onCompleted: {
                text = pyInterface.fileName_qml
            }

            background: Rectangle {
                implicitHeight: text_field_width
                implicitWidth: text_field_height
                color: "white"
                radius: 8
            }
        }

        Button{
            id: submit_spicy_details
            anchors.left: parent.left
            anchors.leftMargin: left_margin
            anchors.top: text_field_filename.bottom
            anchors.topMargin: top_margin
            width: button_width
            height: button_height
            text: qsTr("Submit")
            font.pixelSize: 16
            font.bold: true

            contentItem: Label {
            text: submit_spicy_details.text
            font: submit_spicy_details.font
            color: "white" // Set the text color to white
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
            }

            background: Rectangle {
            color: submit_spicy_details.enabled ? "#1D5992" : "lightgray"
            radius: 10 // Add this line to create rounded edges
            }

            onClicked:{
                pyInterface.get_spicy_values(text_field_api_key.text, text_field_port.text, text_field_filename.text)
            }
            
        }

        Button{
            id: close_server
            anchors.left: parent.left
            anchors.leftMargin: left_margin
            anchors.top: submit_spicy_details.bottom
            anchors.topMargin: top_margin
            width: button_width
            height: button_height
            text: qsTr("Close Server")
            font.pixelSize: 16
            font.bold: true
            background: Rectangle {
            color: close_server.enabled ? "#1D5992" : "lightgray"
            radius: 10 // Add this line to create rounded edges
            }
            contentItem: Label {
            text: close_server.text
            font: close_server.font
            color: "white" // Set the text color to white
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
            }
            onClicked:{
                pyInterface.close_server()
            }
            
        }

        //seperator
        Rectangle {
            id: seperator
            anchors.left: close_server.right
            anchors.leftMargin: 30
            anchors.top: parent.top
            anchors.topMargin: 30
            width: 1
            height: parent.height - 60
            color: "#ffffff"
        }

        Text {
            id: text_enter_prompt
            anchors.left: seperator.right
            anchors.leftMargin: left_margin
            anchors.top: parent.top
            anchors.topMargin: 20
            color: "#ffffff"
            text: qsTr("Enter Prompt:")
            font.pixelSize: 16
            font.bold: true
        }
        TextArea {
            id: text_field_prompt
            anchors.left: seperator.right
            anchors.leftMargin: left_margin
            anchors.top: text_enter_prompt.bottom
            anchors.topMargin: top_margin_sub
            width: 300
            height: 75
            // horizontalAlignment: Text.AlignHCenter
            // verticalAlignment: Text.AlignVCenter
            font.italic: true
            placeholderText: qsTr("Enter Prompt")
            font.pixelSize: 16
            wrapMode: TextEdit.Wrap


            background: Rectangle {
                implicitHeight: text_field_width
                implicitWidth: text_field_height
                color: "white"
                radius: 8
            }
            text:"make a rectrangular plate with a length 20 width of 5 and a height of 10"

        }

        Text {
            id: num_attempts
            anchors.left: seperator.right
            anchors.leftMargin: left_margin
            anchors.top: text_field_prompt.bottom
            anchors.topMargin: top_margin
            color: "#ffffff"
            text: qsTr("No. Attempts :")
            font.pixelSize: 16
            font.bold: true
        }

        TextField {
            id: field_num_attempts
            anchors.left: num_attempts.right
            anchors.leftMargin: left_margin
            // anchors.top: text_field_prompt.bottom
            anchors.verticalCenter: num_attempts.verticalCenter
            width: text_field_width
            height: text_field_height
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
            font.italic: true
            placeholderText: qsTr("1-100")
            font.pixelSize: 16
            background: Rectangle {
                implicitHeight: text_field_width
                implicitWidth: text_field_height
                color: "white"
                radius: 8
            }

            validator:IntValidator {
                bottom: 1
                top: 100
            }
            onTextChanged: {
                var value = parseInt(text);
                if (value < 1 || value > 100) {
                text = ""; }
            }

            text:"10" //remove this line afterwards
        }
        Text {
            id: num_refinement
            anchors.left: seperator.right
            anchors.leftMargin: left_margin
            anchors.top: num_attempts.bottom
            anchors.topMargin: top_margin
            color: "#ffffff"
            text: qsTr("No. Refine :")
            font.pixelSize: 16
            font.bold: true
        }

        TextField {
            id: field_num_refinement
            anchors.left: field_num_attempts.left
            // anchors.leftMargin: left_margin
            // anchors.top: text_field_prompt.bottom
            anchors.verticalCenter: num_refinement.verticalCenter
            width: text_field_width
            height: text_field_height
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
            font.italic: true
            placeholderText: qsTr("1-100")
            font.pixelSize: 16
            background: Rectangle {
                implicitHeight: text_field_width
                implicitWidth: text_field_height
                color: "white"
                radius: 8
            }

            validator:IntValidator {
                bottom: 1
                top: 100
            }
            onTextChanged: {
                var value = parseInt(text);
                if (value < 1 || value > 100) {
                text = ""; }
            }
            text:"5" //remove this line afterwards
        }

        Text {
            id: num_tokens
            anchors.left: seperator.right
            anchors.leftMargin: left_margin
            anchors.top: num_refinement.bottom
            anchors.topMargin: top_margin
            color: "#ffffff"
            text: qsTr("No. Tokens :")
            font.pixelSize: 16
            font.bold: true
        }

        TextField {
            id: field_num_tokens
            anchors.left: field_num_refinement.left
            anchors.leftMargin: 0
            // anchors.top: text_field_prompt.bottom
            anchors.verticalCenter: num_tokens.verticalCenter
            width: text_field_width
            height: text_field_height
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
            font.italic: true
            placeholderText: qsTr("1-4096")
            font.pixelSize: 16
            background: Rectangle {
                implicitHeight: text_field_width
                implicitWidth: text_field_height
                color: "white"
                radius: 8
            }
            validator:IntValidator {
                bottom: 1
                top: 4096
            }
            onTextChanged: {
                var value = parseInt(text);
                if (value < 1 || value > 4096) {
                text = ""; }
            }
            text:"2048" //remove this line afterwards
        }

        Text {
            id: temperature
            anchors.left: seperator.right
            anchors.leftMargin: left_margin
            anchors.top: num_tokens.bottom
            anchors.topMargin: top_margin
            color: "#ffffff"
            text: qsTr("Temperature :")
            font.pixelSize: 16
            font.bold: true
        }

        TextField {
            id: field_temperature
            anchors.left: field_num_attempts.left
            anchors.leftMargin: 0
            // anchors.top: text_field_prompt.bottom
            anchors.verticalCenter: temperature.verticalCenter
            width: text_field_width
            height: text_field_height
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
            font.italic: true
            placeholderText: qsTr("0.0-2.0")
            font.pixelSize: 16
            background: Rectangle {
                implicitHeight: text_field_width
                implicitWidth: text_field_height
                color: "white"
                radius: 8
            }
            validator:DoubleValidator {
                bottom: 0
                top: 2
            }
            onTextChanged: {
                var value = parseFloat(text);
                if (value < 0 || value > 2) {
                text = "1"; }
            }

            text: "1"//remove this
        }

        Text {
            id: presence_penalty    
            anchors.left: seperator.right
            anchors.leftMargin: left_margin
            anchors.top: temperature.bottom
            anchors.topMargin: top_margin
            color: "#ffffff"
            text: qsTr("Presence \nPenalty :")
            font.pixelSize: 16
            font.bold: true
        }

        TextField {
            id: field_pp
            anchors.left: field_num_attempts.left
            anchors.leftMargin: 0
            // anchors.top: text_field_prompt.bottom
            anchors.verticalCenter: presence_penalty.verticalCenter
            width: text_field_width
            height: text_field_height
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
            font.italic: true
            placeholderText: qsTr("-2.0 - 2.0")
            font.pixelSize: 16
            background: Rectangle {
                implicitHeight: text_field_width
                implicitWidth: text_field_height
                color: "white"
                radius: 8
            }
            validator:DoubleValidator {
                bottom: -2
                top: 2
            }
            onTextChanged: {
                var value = parseFloat(text);
                if (value < -2 || value > 2) {
                text = "0"; }
            }
            text:"0" //remove this line afterwards
        }

        Text {
            id: freq_penalty    
            anchors.left: seperator.right
            anchors.leftMargin: left_margin
            anchors.top: field_pp.bottom
            anchors.topMargin: top_margin
            color: "#ffffff"
            text: qsTr("Frequency \nPenalty :")
            font.pixelSize: 16
            font.bold: true
        }

        TextField {
            id: field_fp
            anchors.left: field_num_attempts.left
            anchors.leftMargin: 0
            // anchors.top: text_field_prompt.bottom
            anchors.verticalCenter: freq_penalty.verticalCenter
            width: text_field_width
            height: text_field_height
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
            font.italic: true
            placeholderText: qsTr("-2.0 - 2.0")
            font.pixelSize: 16
            background: Rectangle {
                implicitHeight: text_field_width
                implicitWidth: text_field_height
                color: "white"
                radius: 8
            }
            validator:DoubleValidator {
                bottom: -2
                top: 2
            }
            onTextChanged: {
                var value = parseFloat(text);
                if (value < -2 || value > 2) {
                text = "0"; }
            }
            text:"0" //remove this line afterwards
        }

        Button{
            id: button_generate
            anchors.left: seperator.right
            anchors.leftMargin: left_margin
            anchors.top: freq_penalty.bottom
            anchors.topMargin: 20
            // anchors.right: field_fp.right
            enabled: generateButtonEnabled

            background: Rectangle {
            color: button_generate.enabled ? "#1D5992" : "lightgray"
            radius: 10 // Add this line to create rounded edges
            }

            contentItem: Label {
            text: button_generate.text
            font: button_generate.font
            color: "white" // Set the text color to white
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
            }

            width: 250
            height: 50
            text: qsTr("Generate")
            font.pixelSize: 16
            font.bold: true

            onClicked:{

                pyInterface.get_stuff([text_field_prompt.text, field_num_attempts.text,field_num_refinement.text ,field_num_tokens.text, field_temperature.text, field_pp.text, field_fp.text])

            }
            Connections {
                target: pyInterface
                onGenerate_button_enabled_changed: generateButtonEnabled = enabled
            }

            
        }

        Button{
            id: button_cancel
            anchors.left: button_generate.right
            anchors.leftMargin: 15
            anchors.top: freq_penalty.bottom
            anchors.topMargin: 20
            // anchors.right: field_fp.right
            // enabled: generateButtonEnabled

            background: Rectangle {
            color: button_cancel.enabled ? "crimson" : "lightgray"
            radius: 10 // Add this line to create rounded edges
            }

            contentItem: Label {
            text: button_cancel.text
            font: button_cancel.font
            color: "white" // Set the text color to white
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
            }

            width: 50
            height: 50
            text: qsTr("X")
            font.pixelSize: 16
            font.bold: true

            onClicked: pyInterface.cancel_code_generation()
            
        }

        //seperator
        Rectangle {
            id: seperator2
            anchors.left: text_field_prompt.right
            anchors.leftMargin: 30
            anchors.top: parent.top
            anchors.topMargin: 30
            width: 1
            height: parent.height - 60
            color: "#ffffff"
        }

        Text {
            id: text_results
            anchors.left: seperator2.right
            anchors.leftMargin: left_margin
            anchors.top: parent.top
            anchors.topMargin: 20
            color: "#ffffff"
            text: qsTr("Generated:")
            font.pixelSize: 16
            font.bold: true
        }

        // TextArea{
        //     id: text_area_results
        //     anchors.left: text_results.left
        //     anchors.leftMargin: 0
        //     anchors.top: text_field_prompt.top
        //     // anchors.topMargin: 20
        //     anchors.right: parent.right
        //     anchors.rightMargin: 30
        //     anchors.bottom: parent.bottom
        //     anchors.bottomMargin: 30
        //     color: "black"
        //     text: pyInterface.text_area_results_text
        //     font.pixelSize: 16
        //     font.bold: false
        //     wrapMode: TextEdit.Wrap
        //     readOnly: true
        //     background: Rectangle {
        //         implicitHeight: text_field_width
        //         implicitWidth: text_field_height
        //         color: "white"
        //         radius: 8
        //     }
            
        // }

        // Flickable {
        //     id: textAreaFlickable
        //     anchors.left: text_results.left
        //     anchors.leftMargin: 0
        //     anchors.top: text_field_prompt.top
        //     anchors.right: parent.right
        //     anchors.rightMargin: 30
        //     anchors.bottom: parent.bottom
        //     anchors.bottomMargin: 30
        //     contentWidth: text_area_results.width
        //     contentHeight: text_area_results.contentHeight
        //     clip: true

        //     TextArea {
        //         id: text_area_results
        //         width: textAreaFlickable.width
        //         height: textAreaFlickable.height
        //         color: "black"
        //         text: pyInterface.text_area_results_text
        //         font.pixelSize: 16
        //         font.bold: false
        //         wrapMode: TextEdit.Wrap
        //         readOnly: true
        //         background: Rectangle {
        //             implicitHeight: text_field_width
        //             implicitWidth: text_field_height
        //             color: "white"
        //             radius: 8
        //         }
        //     }
        // }

     

        ScrollView {
            id: scrollView
            anchors.left: text_results.left
            anchors.leftMargin: 0
            anchors.top: text_field_prompt.top
            anchors.right: parent.right
            anchors.rightMargin: 30
            anchors.bottom: parent.bottom
            anchors.bottomMargin: 30
            clip: true

            TextArea {
                id: text_area_results
                width: scrollView.width
                height: scrollView.height
                color: "black"
                text: pyInterface.text_area_results_text
                font.pixelSize: 16
                font.bold: false
                wrapMode: TextEdit.Wrap
                readOnly: true
                background: Rectangle {
                    implicitHeight: text_field_width
                    implicitWidth: text_field_height
                    color: "white"
                    radius: 8
                }
            }
        }






    }
}
