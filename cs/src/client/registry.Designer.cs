namespace client
{
    partial class registry
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.txtReg = new System.Windows.Forms.RichTextBox();
            this.butSend = new System.Windows.Forms.Button();
            this.butBro = new System.Windows.Forms.Button();
            this.txtBro = new System.Windows.Forms.TextBox();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.button1 = new System.Windows.Forms.Button();
            this.opApp = new System.Windows.Forms.ComboBox();
            this.txtKQ = new System.Windows.Forms.RichTextBox();
            this.txtLink = new System.Windows.Forms.TextBox();
            this.txtValue = new System.Windows.Forms.TextBox();
            this.txtNameValue = new System.Windows.Forms.TextBox();
            this.opTypeValue = new System.Windows.Forms.ComboBox();
            this.butXoa = new System.Windows.Forms.Button();
            this.groupBox1.SuspendLayout();
            this.SuspendLayout();
            //
            // txtReg
            //
            this.txtReg.Location = new System.Drawing.Point(2, 55);
            this.txtReg.Name = "txtReg";
            this.txtReg.Size = new System.Drawing.Size(311, 77);
            this.txtReg.TabIndex = 0;
            this.txtReg.Text = "Nội dung";
            //
            // butSend
            //
            this.butSend.Location = new System.Drawing.Point(319, 55);
            this.butSend.Name = "butSend";
            this.butSend.Size = new System.Drawing.Size(75, 77);
            this.butSend.TabIndex = 2;
            this.butSend.Text = "Gởi nội dung";
            this.butSend.UseVisualStyleBackColor = true;
            this.butSend.Click += new System.EventHandler(this.butSend_Click);
            //
            // butBro
            //
            this.butBro.Location = new System.Drawing.Point(319, 20);
            this.butBro.Name = "butBro";
            this.butBro.Size = new System.Drawing.Size(75, 23);
            this.butBro.TabIndex = 4;
            this.butBro.Text = "Browser...";
            this.butBro.UseVisualStyleBackColor = true;
            this.butBro.Click += new System.EventHandler(this.butBro_Click);
            //
            // txtBro
            //
            this.txtBro.Location = new System.Drawing.Point(2, 23);
            this.txtBro.Name = "txtBro";
            this.txtBro.Size = new System.Drawing.Size(311, 20);
            this.txtBro.TabIndex = 5;
            this.txtBro.Text = "Đường dẫn ...";
            //
            // groupBox1
            //
            this.groupBox1.Controls.Add(this.butXoa);
            this.groupBox1.Controls.Add(this.button1);
            this.groupBox1.Controls.Add(this.opApp);
            this.groupBox1.Controls.Add(this.txtKQ);
            this.groupBox1.Controls.Add(this.txtLink);
            this.groupBox1.Controls.Add(this.txtValue);
            this.groupBox1.Controls.Add(this.txtNameValue);
            this.groupBox1.Controls.Add(this.opTypeValue);
            this.groupBox1.Location = new System.Drawing.Point(2, 138);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(384, 204);
            this.groupBox1.TabIndex = 6;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "Sửa giá trị trực tiếp";
            //
            // button1
            //
            this.button1.Location = new System.Drawing.Point(69, 173);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(97, 23);
            this.button1.TabIndex = 6;
            this.button1.Text = "Gởi";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            //
            // opApp
            //
            this.opApp.FormattingEnabled = true;
            this.opApp.Items.AddRange(new object[] {
            "Get value",
            "Set value",
            "Delete value",
            "Create key",
            "Delete key"});
            this.opApp.Location = new System.Drawing.Point(6, 19);
            this.opApp.Name = "opApp";
            this.opApp.Size = new System.Drawing.Size(372, 21);
            this.opApp.TabIndex = 5;
            this.opApp.Text = "Chọn chức năng";
            this.opApp.SelectedIndexChanged += new System.EventHandler(this.comboBox2_SelectedIndexChanged);
            //
            // txtKQ
            //
            this.txtKQ.Enabled = false;
            this.txtKQ.Location = new System.Drawing.Point(6, 99);
            this.txtKQ.Name = "txtKQ";
            this.txtKQ.Size = new System.Drawing.Size(372, 68);
            this.txtKQ.TabIndex = 4;
            this.txtKQ.Text = "";
            //
            // txtLink
            //
            this.txtLink.Location = new System.Drawing.Point(6, 46);
            this.txtLink.Name = "txtLink";
            this.txtLink.Size = new System.Drawing.Size(372, 20);
            this.txtLink.TabIndex = 3;
            this.txtLink.Text = "Đường dẫn";
            //
            // txtValue
            //
            this.txtValue.Location = new System.Drawing.Point(125, 72);
            this.txtValue.Name = "txtValue";
            this.txtValue.Size = new System.Drawing.Size(138, 20);
            this.txtValue.TabIndex = 2;
            this.txtValue.Text = "Vaule";
            //
            // txtNameValue
            //
            this.txtNameValue.Location = new System.Drawing.Point(6, 72);
            this.txtNameValue.Name = "txtNameValue";
            this.txtNameValue.Size = new System.Drawing.Size(113, 20);
            this.txtNameValue.TabIndex = 1;
            this.txtNameValue.Text = "Name value";
            //
            // opTypeValue
            //
            this.opTypeValue.FormattingEnabled = true;
            this.opTypeValue.Items.AddRange(new object[] {
            "String",
            "Binary",
            "DWORD",
            "QWORD",
            "Multi-String",
            "Expandable String"});
            this.opTypeValue.Location = new System.Drawing.Point(269, 72);
            this.opTypeValue.Name = "opTypeValue";
            this.opTypeValue.Size = new System.Drawing.Size(109, 21);
            this.opTypeValue.TabIndex = 0;
            this.opTypeValue.Text = "Kiểu dữ liệu";
            //
            // butXoa
            //
            this.butXoa.Location = new System.Drawing.Point(192, 173);
            this.butXoa.Name = "butXoa";
            this.butXoa.Size = new System.Drawing.Size(94, 23);
            this.butXoa.TabIndex = 7;
            this.butXoa.Text = "Xóa";
            this.butXoa.UseVisualStyleBackColor = true;
            this.butXoa.Click += new System.EventHandler(this.butXoa_Click);
            //
            // registry
            //
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(398, 354);
            this.Controls.Add(this.groupBox1);
            this.Controls.Add(this.txtBro);
            this.Controls.Add(this.butBro);
            this.Controls.Add(this.butSend);
            this.Controls.Add(this.txtReg);
            this.Name = "registry";
            this.Text = "registry";
            this.FormClosing += new System.Windows.Forms.FormClosingEventHandler(this.registry_closing);
            this.groupBox1.ResumeLayout(false);
            this.groupBox1.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.RichTextBox txtReg;
        private System.Windows.Forms.Button butSend;
        private System.Windows.Forms.Button butBro;
        private System.Windows.Forms.TextBox txtBro;
        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.RichTextBox txtKQ;
        private System.Windows.Forms.TextBox txtLink;
        private System.Windows.Forms.TextBox txtValue;
        private System.Windows.Forms.TextBox txtNameValue;
        private System.Windows.Forms.ComboBox opTypeValue;
        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.ComboBox opApp;
        private System.Windows.Forms.Button butXoa;
    }
}