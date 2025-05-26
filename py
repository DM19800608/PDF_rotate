import os
import PyPDF2
from tkinter import Tk, filedialog, messagebox


def rotate_pdf_pages():
    # Initialize Tkinter (hidden root window)
    root = Tk()
    root.withdraw()
    
    # Open file dialog to select PDF
    input_path = filedialog.askopenfilename(
        title="Select PDF to rotate",
        filetypes=[("PDF Files", "*.pdf"), ("All Files", "*.*")]
    )
    
    if not input_path:
        print("No file selected. Exiting.")
        return
    
    # Ask for rotation angle (90° clockwise by default)
    angle = 90  # Default rotation (clockwise)
    while True:
        try:
            user_input = input("Enter rotation angle (90, 180, or 270 degrees): ").strip()
            if not user_input:
                break  # use default
            angle = int(user_input)
            if angle not in (90, 180, 270):
                raise ValueError("Angle must be 90, 180, or 270")
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")
    
    # Create PDF reader and writer objects
    pdf_reader = PyPDF2.PdfReader(input_path)
    pdf_writer = PyPDF2.PdfWriter()
    
    # Rotate each page
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        page.rotate(angle)
        pdf_writer.add_page(page)
    
    # Open save-as dialog
    default_filename = os.path.splitext(os.path.basename(input_path))[0] + "_rotated.pdf"
    output_path = filedialog.asksaveasfilename(
        title="Save rotated PDF as",
        initialfile=default_filename,
        defaultextension=".pdf",
        filetypes=[("PDF Files", "*.pdf"), ("All Files", "*.*")]
    )
    
    if not output_path:
        print("Save cancelled. Exiting.")
        return
    
    # Write the rotated PDF
    try:
        with open(output_path, 'wb') as output_file:
            pdf_writer.write(output_file)
        messagebox.showinfo("Success", f"PDF rotated and saved to:\n{output_path}")
        print(f"Successfully saved rotated PDF to: {output_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save PDF:\n{str(e)}")
        print(f"Error saving PDF: {e}")


if __name__ == "__main__":
    rotate_pdf_pages()
