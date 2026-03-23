import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('equip running')
@cli.command()
def start(): click.echo('equip started')
if __name__ == '__main__': cli()
