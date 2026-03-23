import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('ctop running')
@cli.command()
def start(): click.echo('ctop started')
if __name__ == '__main__': cli()
