import logging
import os.path

from adobe.pdfservices.operation.auth.credentials import Credentials
from adobe.pdfservices.operation.exception.exceptions import ServiceApiException, ServiceUsageException, SdkException
from adobe.pdfservices.operation.pdfops.options.extractpdf.extract_pdf_options import ExtractPDFOptions
from adobe.pdfservices.operation.pdfops.options.extractpdf.extract_element_type import ExtractElementType
from adobe.pdfservices.operation.execution_context import ExecutionContext
from adobe.pdfservices.operation.io.file_ref import FileRef
from adobe.pdfservices.operation.pdfops.extract_pdf_operation import ExtractPDFOperation

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))

try:
    # get base path.
    base_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    # Initial setup, create credentials instance.
    credentials = Credentials.service_principal_credentials_builder(). \
        with_client_id("9187db6a8e7542da8529ce036f8d1a3e"). \
        with_client_secret("p8e-_ha22ILge3Jf-jKsMfPCm8sPG50ZERgK"). \
        build()

    # Create an ExecutionContext using credentials and create a new operation instance.
    execution_context = ExecutionContext.create(credentials)
    extract_pdf_operation = ExtractPDFOperation.create_new()

    # Set operation input from a source file.
    source = FileRef.create_from_local_file("IMG_4072.pdf")
    extract_pdf_operation.set_input(source)

    # Build ExtractPDF options and set them into the operation
    extract_pdf_options: ExtractPDFOptions = ExtractPDFOptions.builder() \
        .with_element_to_extract(ExtractElementType.TEXT) \
        .build()
    extract_pdf_operation.set_options(extract_pdf_options)

    # Execute the operation.
    result: FileRef = extract_pdf_operation.execute(execution_context)

    # Save the result to the specified location.
    result.save_as(base_path + "/output/ExtractTextInfoFromPDF.zip")
except (ServiceApiException, ServiceUsageException, SdkException):
    logging.exception("Exception encountered while executing operation")
