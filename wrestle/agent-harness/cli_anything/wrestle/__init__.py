import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('wrestle running')
@cli.command()
def start(): click.echo('wrestle started')
if __name__ == '__main__': cli()
