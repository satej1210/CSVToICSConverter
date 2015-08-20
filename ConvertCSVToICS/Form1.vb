Public Class Form1
    Dim CSV As String
    Private Sub GenerateICS()
        Dim Summary(100) As String
        Dim StartDate(100) As String
        Dim StartTime(100) As String
        Dim EndDate(100) As String
        Dim EndTime(100) As String
        Dim AllDay(100) As String
        Dim Description(100) As String
        Dim Location(100) As String
        Dim UID(100) As String
        Dim FirstAlert(100) As String
        Dim SecondAlert(100) As String
        Dim ICSArray() As String
        Dim Count As Integer = 0
        ICSArray = Split(CSV, ",")
        For i As Integer = 11 To ICSArray.Length Step 1
            Summary(Count) = ICSArray(i)
            StartDate(Count) = ICSArray(i + 1)
            StartTime(Count) = ICSArray(i + 2)
            EndDate(Count) = ICSArray(i + 3)
            EndTime(Count) = ICSArray(i + 4)
            AllDay(Count) = ICSArray(i + 5)
            Description(Count) = ICSArray(i + 6)
            Location(Count) = ICSArray(i + 7)
            UID(Count) = ICSArray(i + 8)
            FirstAlert(Count) = ICSArray(i + 9)
            SecondAlert(Count) = ICSArray(i + 10)
        Next
    End Sub
    Private Sub Button1_Click(sender As Object, e As EventArgs) Handles Button1.Click
        Dim FileSelect As OpenFileDialog = New OpenFileDialog

        FileSelect.Filter = "Comma Seperated(*.csv)|*.csv"
        FileSelect.FilterIndex = 1
        'Dim UserClickedOK As Boolean = FileSelect.ShowDialog

        ' Process input if the user clicked OK.
        If (FileSelect.ShowDialog() = ShowDialog.OK) Then
            'Open the selected file to read.
            Dim fileStream As System.IO.Stream = FileSelect.OpenFile

            Using reader As New System.IO.StreamReader(fileStream)
                TextBox1.Text = FileSelect.FileName
                ' Read the first line from the file and write it to the text box.
                CSV = reader.Read
                GenerateICS()
            End Using
            fileStream.Close()
        End If
    End Sub

    Private Sub Label3_Click(sender As Object, e As EventArgs) Handles Label3.Click

    End Sub
End Class
