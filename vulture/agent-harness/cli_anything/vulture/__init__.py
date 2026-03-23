import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('vulture running')
@cli.command()
def start(): click.echo('vulture started')
if __name__ == '__main__': cli()
