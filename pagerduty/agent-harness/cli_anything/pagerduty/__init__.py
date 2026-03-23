import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('pagerduty running')
@cli.command()
def start(): click.echo('pagerduty started')
if __name__ == '__main__': cli()
