import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('lerna running')
@cli.command()
def start(): click.echo('lerna started')
if __name__ == '__main__': cli()
