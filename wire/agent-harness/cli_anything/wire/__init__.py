import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('wire running')
@cli.command()
def start(): click.echo('wire started')
if __name__ == '__main__': cli()
