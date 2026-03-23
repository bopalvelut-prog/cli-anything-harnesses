import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('valor running')
@cli.command()
def start(): click.echo('valor started')
if __name__ == '__main__': cli()
