import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('emscripten running')
@cli.command()
def start(): click.echo('emscripten started')
if __name__ == '__main__': cli()
