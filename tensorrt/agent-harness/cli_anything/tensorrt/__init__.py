import click
@click.group()
def cli(): pass
@cli.command()
def build(): click.echo('TensorRT build')
@cli.command()
def engines(): click.echo('TensorRT engines')
if __name__ == '__main__': cli()
