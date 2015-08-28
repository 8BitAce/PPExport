from gooey import Gooey
from gooey import GooeyParser
import argparse

import os
import comtypes.client

def export_presentation(ppt, outdir, width, height):
    powerpoint = comtypes.client.CreateObject("Powerpoint.Application")
    powerpoint.Visible = True
    powerpoint.Presentations.Open(ppt)
    powerpoint.ActivePresentation.Export(outdir, "JPG", int(width), int(height))
    powerpoint.Presentations[1].Close()
    powerpoint.Quit()
    

@Gooey
def main():
    parser = GooeyParser(description="PowerPoint Exporter")
    parser.add_argument('powerpoint', widget="FileChooser")
    parser.add_argument('output', help="Folder to place resulting images", widget="DirChooser")
    parser.add_argument('width', help="Width of resulting image (0-3072)")
    parser.add_argument('height', help="Height of resulting image (0-3072)")
    args = parser.parse_args()

    if not (os.path.isfile(args.powerpoint) and os.path.isdir(args.output)):
        raise "Invalid paths!"

    export_presentation(args.powerpoint, args.output, args.width, args.height)

    print "Done!"
    
if __name__ == "__main__":
    main()
