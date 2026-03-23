import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('rustup running')
@cli.command()
def start(): click.echo('rustup started')
if __name__ == '__main__': cli()
