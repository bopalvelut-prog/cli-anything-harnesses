import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('healthcheck running')
@cli.command()
def start(): click.echo('healthcheck started')
if __name__ == '__main__': cli()
