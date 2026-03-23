import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('twice running')
@cli.command()
def start(): click.echo('twice started')
if __name__ == '__main__': cli()
