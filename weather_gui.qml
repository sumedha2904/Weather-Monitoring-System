import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ApplicationWindow {

    visible: true
    width: 700
    height: 500

    title: "Weather Monitoring System"

    ColumnLayout {

        anchors.fill: parent
        anchors.margins: 30
        spacing: 20

        Text {
            text: "WEATHER MONITORING SYSTEM"

            Layout.alignment: Qt.AlignHCenter

            color: "white"
            font.pixelSize: 24
            font.bold: true
        }

        RowLayout {

            Layout.alignment: Qt.AlignHCenter
            spacing: 20

            Button {
                text: "Connect"

                onClicked: {
                    backend.connect_to_esp32()
                }
            }

            Button {
                text: "Disconnect"

                onClicked: {
                    backend.disconnect_from_esp32()
                }
            }
        }

        GridLayout {

            id: readingsGrid

            Layout.fillWidth: true
            Layout.fillHeight: true

            columns: 2
            rows: 2

            columnSpacing: 15
            rowSpacing: 15

            Rectangle {
                id: box1

                Layout.fillWidth: true
                Layout.fillHeight: true

                color: "#252525"
                radius: 10
                border.width: 1
                border.color: "gray"

                Text {
                    id: text1

                    anchors.centerIn: parent

                    width: parent.width - 30

                    color: "white"
                    font.pixelSize: 16

                    horizontalAlignment: Text.AlignHCenter
                    wrapMode: Text.Wrap
                }
            }

            Rectangle {
                id: box2

                Layout.fillWidth: true
                Layout.fillHeight: true

                color: "#252525"
                radius: 10
                border.width: 1
                border.color: "gray"

                Text {
                    id: text2

                    anchors.centerIn: parent

                    width: parent.width - 30

                    color: "white"
                    font.pixelSize: 16

                    horizontalAlignment: Text.AlignHCenter
                    wrapMode: Text.Wrap
                }
            }

            Rectangle {
                id: box3

                Layout.fillWidth: true
                Layout.fillHeight: true

                color: "#252525"
                radius: 10
                border.width: 1
                border.color: "gray"

                Text {
                    id: text3

                    anchors.centerIn: parent

                    width: parent.width - 30

                    color: "white"
                    font.pixelSize: 16

                    horizontalAlignment: Text.AlignHCenter
                    wrapMode: Text.Wrap
                }
            }

            Rectangle {
                id: box4

                Layout.fillWidth: true
                Layout.fillHeight: true

                color: "#252525"
                radius: 10
                border.width: 1
                border.color: "gray"

                Text {
                    id: text4

                    anchors.centerIn: parent

                    width: parent.width - 30

                    color: "white"
                    font.pixelSize: 16

                    horizontalAlignment: Text.AlignHCenter
                    wrapMode: Text.Wrap
                }
            }
        }
    }

    property int currentBox: 0

    Connections {

        target: backend

        function onReading_received(jsonData) {

            if (currentBox == 0) {
                text1.text = jsonData
            }
            else if (currentBox == 1) {
                text2.text = jsonData
            }
            else if (currentBox == 2) {
                text3.text = jsonData
            }
            else {
                text4.text = jsonData
            }
            currentBox = (currentBox + 1) % 4
        }
    }
}