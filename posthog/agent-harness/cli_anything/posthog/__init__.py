import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('posthog running')
@cli.command()
def start(): click.echo('posthog started')
if __name__ == '__main__': cli()
