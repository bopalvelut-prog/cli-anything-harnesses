import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('application_insights running')
@cli.command()
def start(): click.echo('application_insights started')
if __name__ == '__main__': cli()
