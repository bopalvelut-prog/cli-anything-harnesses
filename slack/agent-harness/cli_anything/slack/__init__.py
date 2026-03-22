import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def send(): click.echo('Slack message sent')
@cli.command()
def channels(): click.echo('Slack channels')
if __name__ == '__main__': cli()
