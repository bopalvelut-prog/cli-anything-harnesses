import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('atlassian_opsgenie running')
@cli.command()
def start(): click.echo('atlassian_opsgenie started')
if __name__ == '__main__': cli()
