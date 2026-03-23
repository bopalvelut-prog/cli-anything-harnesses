import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('launchdarkly running')
@cli.command()
def start(): click.echo('launchdarkly started')
if __name__ == '__main__': cli()
