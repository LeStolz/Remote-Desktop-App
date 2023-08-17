namespace client
{
    partial class Kill
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
            this.butNhap = new System.Windows.Forms.Button();
            this.txtID = new System.Windows.Forms.TextBox();
            this.SuspendLayout();
            // 
            // butNhap
            // 
            this.butNhap.Location = new System.Drawing.Point(202, 13);
            this.butNhap.Name = "butNhap";
            this.butNhap.Size = new System.Drawing.Size(75, 23);
            this.butNhap.TabIndex = 0;
            this.butNhap.Text = "Kill";
            this.butNhap.UseVisualStyleBackColor = true;
            this.butNhap.Click += new System.EventHandler(this.butNhap_Click);
            // 
            // txtID
            // 
            this.txtID.Location = new System.Drawing.Point(13, 13);
            this.txtID.Name = "txtID";
            this.txtID.Size = new System.Drawing.Size(183, 20);
            this.txtID.TabIndex = 1;
            this.txtID.Text = "Nhập ID";
            // 
            // Kill
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(284, 45);
            this.Controls.Add(this.txtID);
            this.Controls.Add(this.butNhap);
            this.Name = "Kill";
            this.Text = "Kill";
            this.FormClosing += new System.Windows.Forms.FormClosingEventHandler(this.kill_closing);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button butNhap;
        private System.Windows.Forms.TextBox txtID;
    }
}