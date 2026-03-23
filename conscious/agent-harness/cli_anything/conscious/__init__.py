import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('conscious running')
@cli.command()
def start(): click.echo('conscious started')
if __name__ == '__main__': cli()
