import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('google_tasks running')
@cli.command()
def start(): click.echo('google_tasks started')
if __name__ == '__main__': cli()
