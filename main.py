# V7 Scan all DICOM files in a series, no error checking
import pydicom
import os


def write_corrected_dicom(dicom_file_path, output_dir):

    ds = pydicom.dcmread(dicom_file_path, force=True)

    # Convert ds into a string
    _ = str(ds)

    # Create directory for corrected DICOM file
    os.makedirs(output_dir, exist_ok=True)

    # Save the corrected DICOM file
    corrected_file_path = os.path.join(output_dir, os.path.basename(dicom_file_path))
    ds.save_as(corrected_file_path)
    print(f"Corrected DICOM file saved to {corrected_file_path}")


def correct_dicom_files_in_series(series_dir):

    for root, _, files in os.walk(series_dir):
        for file in files:
            dicom_file_path = os.path.join(root, file)
            output_dir = os.path.join(root + "-corrected")
            write_corrected_dicom(dicom_file_path, output_dir)


# Change the working directory
os.chdir("/Users/alrubayehayder/Downloads/PHI/error-pydicom-studies")

dicom_series = input("Enter the series ID: ")

series_dir = os.path.join(".", dicom_series)

correct_dicom_files_in_series(series_dir)
