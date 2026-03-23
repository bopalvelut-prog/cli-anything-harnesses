import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('byteman running')
@cli.command()
def start(): click.echo('byteman started')
if __name__ == '__main__': cli()
