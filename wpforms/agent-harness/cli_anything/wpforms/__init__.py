import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def forms(): click.echo('WPForms forms')
@cli.command()
def entries(): click.echo('WPForms entries')
if __name__ == '__main__': cli()
