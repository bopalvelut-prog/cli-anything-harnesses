import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('brightness running')
@cli.command()
def start(): click.echo('brightness started')
if __name__ == '__main__': cli()
