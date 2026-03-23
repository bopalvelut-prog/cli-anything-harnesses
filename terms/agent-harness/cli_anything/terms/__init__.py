import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('terms running')
@cli.command()
def start(): click.echo('terms started')
if __name__ == '__main__': cli()
