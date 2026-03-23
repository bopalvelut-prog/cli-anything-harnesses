import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('note running')
@cli.command()
def start(): click.echo('note started')
if __name__ == '__main__': cli()
