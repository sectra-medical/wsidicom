#    Copyright 2021, 2022, 2023 SECTRA AB
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


from wsidicom.file.io.frame_index.bot import Bot, EmptyBotException
from wsidicom.file.io.frame_index.empty_bot import EmptyBot
from wsidicom.file.io.frame_index.eot import Eot
from wsidicom.file.io.frame_index.frame_index import FrameIndex
from wsidicom.file.io.frame_index.native_pixel_data_frame import NativePixelData
from wsidicom.file.io.frame_index.offset_table_type import OffsetTableType
from wsidicom.file.io.frame_index.offset_table_writer import (
    BotWriter,
    EotWriter,
    OffsetTableWriter,
)
