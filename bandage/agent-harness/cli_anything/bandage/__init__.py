import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('bandage running')
@cli.command()
def start(): click.echo('bandage started')
if __name__ == '__main__': cli()
