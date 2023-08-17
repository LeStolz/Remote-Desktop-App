namespace client
{
    partial class client
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
            this.butApp = new System.Windows.Forms.Button();
            this.butConnect = new System.Windows.Forms.Button();
            this.txtIP = new System.Windows.Forms.TextBox();
            this.butTat = new System.Windows.Forms.Button();
            this.butReg = new System.Windows.Forms.Button();
            this.butExit = new System.Windows.Forms.Button();
            this.butPic = new System.Windows.Forms.Button();
            this.butKeyLock = new System.Windows.Forms.Button();
            this.butProcess = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // butApp
            // 
            this.butApp.Location = new System.Drawing.Point(93, 64);
            this.butApp.Name = "butApp";
            this.butApp.Size = new System.Drawing.Size(145, 63);
            this.butApp.TabIndex = 0;
            this.butApp.Text = "App Running";
            this.butApp.UseVisualStyleBackColor = true;
            this.butApp.Click += new System.EventHandler(this.butApp_Click);
            // 
            // butConnect
            // 
            this.butConnect.Location = new System.Drawing.Point(244, 27);
            this.butConnect.Name = "butConnect";
            this.butConnect.Size = new System.Drawing.Size(100, 23);
            this.butConnect.TabIndex = 1;
            this.butConnect.Text = "Kết nối";
            this.butConnect.UseVisualStyleBackColor = true;
            this.butConnect.Click += new System.EventHandler(this.butConnect_Click);
            // 
            // txtIP
            // 
            this.txtIP.Location = new System.Drawing.Point(12, 29);
            this.txtIP.Name = "txtIP";
            this.txtIP.Size = new System.Drawing.Size(226, 20);
            this.txtIP.TabIndex = 2;
            this.txtIP.Text = "Nhập IP";
            // 
            // butTat
            // 
            this.butTat.Location = new System.Drawing.Point(93, 133);
            this.butTat.Name = "butTat";
            this.butTat.Size = new System.Drawing.Size(48, 57);
            this.butTat.TabIndex = 4;
            this.butTat.Text = "Tắt máy";
            this.butTat.UseVisualStyleBackColor = true;
            this.butTat.Click += new System.EventHandler(this.button1_Click);
            // 
            // butReg
            // 
            this.butReg.Location = new System.Drawing.Point(93, 196);
            this.butReg.Name = "butReg";
            this.butReg.Size = new System.Drawing.Size(198, 65);
            this.butReg.TabIndex = 5;
            this.butReg.Text = "Sửa registry";
            this.butReg.UseVisualStyleBackColor = true;
            this.butReg.Click += new System.EventHandler(this.butReg_Click);
            // 
            // butExit
            // 
            this.butExit.Location = new System.Drawing.Point(297, 196);
            this.butExit.Name = "butExit";
            this.butExit.Size = new System.Drawing.Size(47, 65);
            this.butExit.TabIndex = 6;
            this.butExit.Text = "Thoát";
            this.butExit.UseVisualStyleBackColor = true;
            this.butExit.Click += new System.EventHandler(this.butExit_Click);
            // 
            // butPic
            // 
            this.butPic.Location = new System.Drawing.Point(147, 133);
            this.butPic.Name = "butPic";
            this.butPic.Size = new System.Drawing.Size(91, 57);
            this.butPic.TabIndex = 7;
            this.butPic.Text = "Chụp màn hình";
            this.butPic.UseVisualStyleBackColor = true;
            this.butPic.Click += new System.EventHandler(this.butPic_Click);
            // 
            // butKeyLock
            // 
            this.butKeyLock.Location = new System.Drawing.Point(244, 64);
            this.butKeyLock.Name = "butKeyLock";
            this.butKeyLock.Size = new System.Drawing.Size(100, 126);
            this.butKeyLock.TabIndex = 8;
            this.butKeyLock.Text = "Keystroke";
            this.butKeyLock.UseVisualStyleBackColor = true;
            this.butKeyLock.Click += new System.EventHandler(this.butKeyLock_Click);
            // 
            // butProcess
            // 
            this.butProcess.Location = new System.Drawing.Point(12, 64);
            this.butProcess.Name = "butProcess";
            this.butProcess.Size = new System.Drawing.Size(75, 197);
            this.butProcess.TabIndex = 9;
            this.butProcess.Text = "Process Running";
            this.butProcess.UseVisualStyleBackColor = true;
            this.butProcess.Click += new System.EventHandler(this.butProcess_Click);
            // 
            // client
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(372, 302);
            this.Controls.Add(this.butProcess);
            this.Controls.Add(this.butKeyLock);
            this.Controls.Add(this.butPic);
            this.Controls.Add(this.butExit);
            this.Controls.Add(this.butReg);
            this.Controls.Add(this.butTat);
            this.Controls.Add(this.txtIP);
            this.Controls.Add(this.butConnect);
            this.Controls.Add(this.butApp);
            this.Name = "client";
            this.Text = "Client";
            this.FormClosing += new System.Windows.Forms.FormClosingEventHandler(this.client_Closing);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button butApp;
        private System.Windows.Forms.Button butConnect;
        private System.Windows.Forms.TextBox txtIP;
        private System.Windows.Forms.Button butTat;
        private System.Windows.Forms.Button butReg;
        private System.Windows.Forms.Button butExit;
        private System.Windows.Forms.Button butPic;
        private System.Windows.Forms.Button butKeyLock;
        private System.Windows.Forms.Button butProcess;
    }
}

