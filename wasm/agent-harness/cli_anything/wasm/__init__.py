import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('wasm running')
@cli.command()
def start(): click.echo('wasm started')
if __name__ == '__main__': cli()
