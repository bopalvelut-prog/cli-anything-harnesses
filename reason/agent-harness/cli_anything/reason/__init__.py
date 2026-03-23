import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('reason running')
@cli.command()
def start(): click.echo('reason started')
if __name__ == '__main__': cli()
