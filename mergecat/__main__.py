import click


@click.command()
@click.option("--input",
              prompt="Video file to process",
              help="Location of video file to process")
def mergecat(video_file):
    click.echo("Hello world!")


if __name__ == '__main__':
    mergecat()
