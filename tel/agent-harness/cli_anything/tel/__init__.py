import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('tel running')
@cli.command()
def start(): click.echo('tel started')
if __name__ == '__main__': cli()
