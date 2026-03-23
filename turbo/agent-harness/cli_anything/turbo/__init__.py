import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('turbo running')
@cli.command()
def start(): click.echo('turbo started')
if __name__ == '__main__': cli()
