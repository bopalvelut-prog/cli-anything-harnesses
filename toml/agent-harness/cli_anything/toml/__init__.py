import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('toml running')
@cli.command()
def start(): click.echo('toml started')
if __name__ == '__main__': cli()
