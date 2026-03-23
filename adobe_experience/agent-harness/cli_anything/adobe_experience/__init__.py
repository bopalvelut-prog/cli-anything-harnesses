import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('adobe_experience running')
@cli.command()
def start(): click.echo('adobe_experience started')
if __name__ == '__main__': cli()
