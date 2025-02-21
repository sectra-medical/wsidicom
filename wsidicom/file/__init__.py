#    Copyright 2023 SECTRA AB
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

"""Module for handling DICOM WSI instances read from file."""

from wsidicom.file.io.frame_index import OffsetTableType
from wsidicom.file.wsidicom_file_source import WsiDicomFileSource
from wsidicom.file.wsidicom_file_target import WsiDicomFileTarget
