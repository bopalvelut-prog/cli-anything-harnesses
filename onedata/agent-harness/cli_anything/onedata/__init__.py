import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('onedata running')
@cli.command()
def start(): click.echo('onedata started')
if __name__ == '__main__': cli()
