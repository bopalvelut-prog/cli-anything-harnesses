import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('sidekiq running')
@cli.command()
def start(): click.echo('sidekiq started')
if __name__ == '__main__': cli()
