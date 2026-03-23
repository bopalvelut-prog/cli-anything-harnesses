import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('halide running')
@cli.command()
def start(): click.echo('halide started')
if __name__ == '__main__': cli()
